from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.card_effects.passives_common import protect_next_turn

card = PokemonCardDef(
    guid="dbee864e-2a1b-5afd-9eae-2840b98ef2a3",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegielekiV.Name",
    display_name="Regieleki V",
    searchable_by=["Regieleki V", "Basic", "V", "RegielekiV"],
    subtypes=["Basic", "V"],
    collector_number=175,
    set_code="SWSH12",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=894,
    abilities=[
        Attack(
            title="Switching Bolt",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=switch_self_attack(),
        ),
        Attack(
            title="Lightning Wall",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 100 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=protect_next_turn(reduce=100),
        ),
    ],
)