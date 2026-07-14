from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_bench


def _no_stadium_in_play(board, player_id, pokemon):
    stadium_area = board.find_global_area("activeStadium")
    return not (stadium_area and stadium_area.children)


card = PokemonCardDef(
    guid="74cdc778-8cf6-5bd3-9c32-a42fd67dfb5d",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slaking.Name",
    display_name="Slaking",
    searchable_by=["Slaking", "Stage 2", "Single Strike", "Slaking"],
    subtypes=["Stage 2", "Single Strike"],
    collector_number=131,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    family_id=287,
    abilities=[
        Ability(
            title="Act Freely",
            game_text="If a Stadium is in play, this Pok\u00e9mon can't attack.",
        ),
        Attack(
            title="Rout",
            game_text="This attack does 30 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            damage_operator="+",
            condition=_no_stadium_in_play,
            effect=damage_per(count_bench("opponent"), 30, base=120),
        ),
    ],
)