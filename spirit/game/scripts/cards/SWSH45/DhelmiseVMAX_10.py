from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy


async def swinging_chain(ctx):
    amount = 30 * count_energy("self", energy_type=PokemonTypes.GRASS)(ctx)
    if amount <= 0:
        return
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    target = await ctx.choose_pokemon(candidates, "Choose 1 of your opponent's Pokémon")
    if target is not None:
        await ctx.deal_damage(amount, target=target)


card = PokemonCardDef(
    guid="64878312-a93f-5b53-ab2d-255fd5bf5529",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DhelmiseVMAX.Name",
    display_name="Dhelmise VMAX",
    searchable_by=["Dhelmise VMAX", "VMAX", "DhelmiseVMAX"],
    subtypes=["VMAX"],
    collector_number=10,
    set_code="SWSH45",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DhelmiseV.Name",
    family_id=781,
    abilities=[
        Attack(
            title="Swinging Chain",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon for each Grass Energy attached to this Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            effect=swinging_chain,
        ),
        Attack(
            title="Max Anchor",
            game_text="During your next turn, this Pok\u00e9mon can't use Max Anchor.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=240,
            locks_next_turn=True,
        ),
    ],
)