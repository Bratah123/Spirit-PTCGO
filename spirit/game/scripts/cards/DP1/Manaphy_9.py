from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import call_for_family_basic
from spirit.game.card_effects.support_common import switch_self_attack


card = PokemonCardDef(
    guid="f536fbc7-761f-53c4-9599-c5696c049196",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy", "Basic", "Manaphy"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="DP1",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=490,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=call_for_family_basic(),
        ),
        Attack(
            title="Aqua Ring",
            game_text="Switch Manaphy with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=switch_self_attack(damage=30, optional=False),
        ),
    ],
)
