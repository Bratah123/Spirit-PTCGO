from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack

card = PokemonCardDef(
    guid="8ca70d54-0103-51d2-af39-8354e1a2620d",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianElectrode.Name",
    display_name="Hisuian Electrode",
    searchable_by=["Hisuian Electrode", "Stage 1", "HisuianElectrode"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianVoltorb.Name",
    family_id=100,
    abilities=[
        Attack(
            title="Triple Draw",
            game_text="Draw 3 cards.",
            cost={},
            effect=draw_attack(3),
        ),
        Attack(
            title="Irritated Bomb",
            cost={},
            damage=50,
        ),
    ],
)