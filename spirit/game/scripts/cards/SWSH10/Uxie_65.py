from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="23f46731-1a90-5169-85cd-698638080abc",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Uxie.Name",
    display_name="Uxie",
    searchable_by=["Uxie", "Basic", "Uxie"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=480,
    abilities=[
        Attack(
            title="Wise Guidance",
            game_text="Search your deck for a card and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(count=1, minimum=0, reveal=False),
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)