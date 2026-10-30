from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per


card = PokemonCardDef(
    guid="fe9e3517-87fc-50cd-b38d-de630e59a181",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeon.Name",
    display_name="Espeon",
    searchable_by=["Espeon", "Stage 1", "Espeon"],
    subtypes=["Stage 1"],
    collector_number=1,
    set_code="NEO2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Psychic",
            game_text="Does 30 damage plus 10 more damage for each Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_energy("defender", cards=True), 10, base=30),
        ),
    ],
)
