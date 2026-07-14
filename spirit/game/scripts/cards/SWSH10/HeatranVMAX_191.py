from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import effective_max_hp


def _magma_gain_condition(board, player_id, pokemon):
    stadium_area = board.find_global_area("activeStadium")
    if not (stadium_area and stadium_area.children):
        return False
    return pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)


async def _magma_gain(ctx):
    if await ctx.ask_yes_no("Heal 50 damage from this Pokémon?"):
        await ctx.heal(50, ctx.source)

card = PokemonCardDef(
    guid="46c8d36e-0749-56ba-afd7-459c79c7e575",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HeatranVMAX.Name",
    display_name="Heatran VMAX",
    searchable_by=["Heatran VMAX", "VMAX", "HeatranVMAX"],
    subtypes=["VMAX"],
    collector_number=191,
    set_code="SWSH10",
    rarity=Rarities.RareRainbow,
    hp=330,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.VMAX,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HeatranV.Name",
    family_id=485,
    abilities=[
        Ability(
            title="Magma Gain",
            game_text="Once during your turn, if you have a Stadium in play, you may heal 50 damage from this Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_magma_gain_condition,
            effect=_magma_gain,
        ),
        Attack(
            title="Max Heat Burst",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
    ],
)