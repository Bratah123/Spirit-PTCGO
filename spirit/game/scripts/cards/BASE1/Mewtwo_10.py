from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.ecard import barrier, has_psychic_energy_attached


card = PokemonCardDef(
    guid="ddb931c8-0c77-555e-baeb-a473c7266c75",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    display_name="Mewtwo",
    searchable_by=["Mewtwo", "Basic", "Mewtwo"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="BASE1",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Psychic",
            game_text="Does 10 damage plus 10 more damage for each Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_energy("defender", cards=True), 10, base=10),
        ),
        Attack(
            title="Barrier",
            game_text="Discard 1 Psychic Energy card attached to Mewtwo in order to prevent all effects of attacks, including damage, done to Mewtwo during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 2},
            condition=has_psychic_energy_attached,
            effect=barrier,
        ),
    ],
)
