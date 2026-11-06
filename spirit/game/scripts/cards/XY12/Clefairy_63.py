from spirit.game.data_utils import PokemonCardDef, Attack, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def nine_tailed_shapeshifter(ctx):
    """Choose 1 of the opponent's Active Pokemon's attacks and use it."""
    defender = ctx.defender
    if defender is None:
        return
    definition = def_for(defender.archetype_id)
    attacks = [a for a in getattr(definition, "abilities", []) if isinstance(a, Attack)]
    if not attacks:
        return
    candidates = [(defender, atk) for atk in attacks]
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    await ctx.use_attack(chosen)


card = PokemonCardDef(
    guid="131d5298-96ee-54bb-b5be-00e62c4cfd75",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    display_name="Clefairy",
    searchable_by=["Clefairy", "Basic", "Clefairy"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="XY12",
    rarity=Rarities.RareHolo,
    hp=40,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=35,
    abilities=[
        Attack(
            title="Sing",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
        Attack(
            title="Metronome",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=nine_tailed_shapeshifter,
        ),
    ],
)