from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(
    guid="5b5f104b-acdc-5ff8-a933-36c815d33749",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zeraora.Name",
    display_name="Zeraora",
    searchable_by=["Zeraora", "Basic", "Zeraora"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="CZ",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=807,
    abilities=[
        Attack(
            title="Wild Charge",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=recoil_attack(20),
        ),
    ],
)
