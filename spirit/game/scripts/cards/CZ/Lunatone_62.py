from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import read_the_wind
from spirit.game.card_effects.attacks_common import damage_per, count_energy

card = PokemonCardDef(
    guid="2629a956-6b0c-58b5-a372-91927fa03c96",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name",
    display_name="Lunatone",
    searchable_by=["Lunatone", "Basic", "Lunatone"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="CZ",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=337,
    abilities=[
        Attack(
            title="Cycle Draw",
            game_text="Discard a card from your hand. If you do, draw 3 cards.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=read_the_wind,
        ),
        Attack(
            title="Moon Kinesis",
            game_text="This attack does 30 more damage for each Psychic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_energy("self", energy_type=PokemonTypes.PSYCHIC.value), 30),
        ),
    ],
)