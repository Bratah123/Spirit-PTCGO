from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm12 import dance_of_tribute, dance_of_tribute_condition
from spirit.game.card_effects.sm3 import crossing_cut_gx


card = PokemonCardDef(
    guid="1f5f8315-f7e4-54c3-9ab1-b5f04cddf23a",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OricorioGX.Name",
    display_name="Oricorio-GX",
    searchable_by=["Oricorio-GX", "Basic", "GX", "OricorioGX"],
    subtypes=["Basic", "GX"],
    collector_number=217,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=741,
    abilities=[
        Ability(
            title="Dance of Tribute",
            game_text="Once during your turn (before your attack), if any of your Pok\u00e9mon were Knocked Out during your opponent's last turn, you may draw 3 cards. You can't use more than 1 Dance of Tribute Ability each turn.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Dance of Tribute",
            condition=dance_of_tribute_condition,
            effect=dance_of_tribute,
        ),
        Attack(
            title="Razor Wing",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
        Attack(
            title="Strafe-GX",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=crossing_cut_gx,
        ),
    ],
)