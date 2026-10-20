from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack


card = PokemonCardDef(
    guid="79c28756-481d-582a-b79d-8f1cb573c5a4",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MLucarioEX.Name",
    display_name="M Lucario-EX",
    searchable_by=["M Lucario-EX", "MEGA", "EX", "MLucarioEX"],
    subtypes=["MEGA", "EX"],
    collector_number=113,
    set_code="XY3",
    rarity=Rarities.RareSecret,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LucarioEX.Name",
    family_id=448,
    abilities=[
        Attack(
            title="Rising Fist",
            game_text="Discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=140,
            effect=discard_opponent_energy_attack(),
        ),
    ],
)