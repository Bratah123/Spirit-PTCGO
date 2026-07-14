from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


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
    guid="0be33e94-0136-536a-8d7f-64b883d11f7c",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NinetalesV.Name",
    display_name="Ninetales V",
    searchable_by=["Ninetales V", "Basic", "V", "NinetalesV"],
    subtypes=["Basic", "V"],
    collector_number=177,
    set_code="SWSH2",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=38,
    abilities=[
        Attack(
            title="Nine-Tailed Shapeshifter",
            game_text="Choose 1 of your opponent's Active Pokémon's attacks and use it as this attack.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            effect=nine_tailed_shapeshifter,
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)
