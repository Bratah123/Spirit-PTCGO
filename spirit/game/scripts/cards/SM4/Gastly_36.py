from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import place_counters


card = PokemonCardDef(
    guid="f6d913ce-e56a-5fa7-81cd-d9f36d2ec730",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    display_name="Gastly",
    searchable_by=["Gastly", "Basic", "Gastly"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="SM4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=92,
    abilities=[
        Attack(
            title="Ominous Eyes",
            game_text="Put 1 damage counter on 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=place_counters(1, 'choose_any_opponent'),
        ),
    ],
)