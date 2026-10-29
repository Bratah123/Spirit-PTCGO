from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench

card = PokemonCardDef(
    guid="423f7a54-aefd-529f-9930-17cc1f68d957",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Salandit.Name",
    display_name="Salandit",
    searchable_by=["Salandit", "Basic", "Salandit"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="DM",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=757,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(),
        ),
        Attack(
            title="Dig Claws",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)