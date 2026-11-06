from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.ecard import unused_energy_bonus


card = PokemonCardDef(
    guid="60af75bb-dcea-5e8c-8597-3ac99f2db0f6",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    display_name="Psyduck",
    searchable_by=["Psyduck", "Basic", "Psyduck"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="BASE6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=54,
    abilities=[
        Attack(
            title="Dizziness",
            game_text="Draw a card.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=draw_attack(1),
        ),
        Attack(
            title="Water Gun",
            game_text="Does 20 damage plus 10 more damage for each Water Energy attached to Psyduck but not used to pay for this attack's Energy cost. You can't add more than 20 damage in this way.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unused_energy_bonus(10, 20, energy_type=PokemonTypes.WATER),
        ),
    ],
)
