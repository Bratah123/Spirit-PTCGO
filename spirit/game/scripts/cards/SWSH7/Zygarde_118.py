from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_prizes_taken


async def judgment_surge(ctx):
    """40 damage to 1 of your opponent's Pokemon for each Prize card your
    opponent has taken. (No W/R for a Benched target -- engine default.)"""
    amount = 40 * count_prizes_taken("opponent")(ctx)
    if amount <= 0:
        return
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    target = await ctx.choose_pokemon(candidates, "Choose 1 of your opponent's Pokémon")
    if target is not None:
        await ctx.deal_damage(amount, target=target)


card = PokemonCardDef(
    guid="5e905c75-3ffb-56f0-8f7a-160f098b09f1",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zygarde.Name",
    display_name="Zygarde",
    searchable_by=["Zygarde", "Basic", "Rapid Strike", "Zygarde"],
    subtypes=["Basic", "Rapid Strike"],
    collector_number=118,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=718,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Judgment Surge",
            game_text="This attack does 40 damage to 1 of your opponent's Pok\u00e9mon for each Prize card your opponent has taken. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            effect=judgment_surge,
        ),
    ],
)