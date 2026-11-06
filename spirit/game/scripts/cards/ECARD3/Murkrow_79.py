from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import place_counters
from spirit.game.card_effects.ecard import blindside


card = PokemonCardDef(
    guid="890c5365-cc5f-5bfb-a628-2846764dda62",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    display_name="Murkrow",
    searchable_by=["Murkrow", "Basic", "Murkrow"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=198,
    abilities=[
        Attack(
            title="Evil Eye",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. Put a damage counter on that Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=place_counters(1, target="choose_any_opponent"),
        ),
        Attack(
            title="Blindside",
            game_text="Choose 1 of your opponent's Pok\u00e9mon that has a damage counter on it. This attack does 20 damage to that Pok\u00e9mon. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=blindside,
        ),
    ],
)
