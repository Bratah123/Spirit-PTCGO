from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import switch_self_attack


card = PokemonCardDef(
    guid="d7d523dd-18a5-5f4f-910f-859fb0f11ef9",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name",
    display_name="Horsea",
    searchable_by=["Horsea", "Basic", "Horsea"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=116,
    abilities=[
        Attack(
            title="Reverse Thrust",
            game_text="Switch Horsea with 1 of your Benched Pok\u00e9mon, if any.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=switch_self_attack(),
        ),
    ],
)
