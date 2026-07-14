from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import place_counters

card = PokemonCardDef(
    guid="4e6c4e23-e8d2-56e2-a4e8-1423b8c15a0c",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianCorsola.Name",
    display_name="Galarian Corsola",
    searchable_by=["Galarian Corsola", "Basic", "GalarianCorsola"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="SWSH2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=222,
    abilities=[
        Attack(
            title="Cursed Drop",
            game_text="Put 3 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=place_counters(3, "choose_any_opponent"),
        ),
    ],
)