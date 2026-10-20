from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn

card = PokemonCardDef(
    guid="83440cca-acb7-5fac-bfc0-3f72bdb8b446",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    display_name="Cottonee",
    searchable_by=["Cottonee", "Basic", "Cottonee"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="BW2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=546,
    abilities=[
        Attack(
            title="Cotton Guard",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 10 (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=protect_next_turn(reduce=10),
        ),
    ],
)
