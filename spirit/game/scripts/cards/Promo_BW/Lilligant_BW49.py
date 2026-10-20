from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_supporter_card


card = PokemonCardDef(
    guid="b6d43646-bbcb-5b35-858f-8ecdde5d6b13",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lilligant.Name",
    display_name="Lilligant",
    searchable_by=["Lilligant", "Stage 1", "Lilligant"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name",
    family_id=549,
    abilities=[
        Attack(
            title="Lead",
            game_text="Search your deck for a Supporter card, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_supporter_card, count=1, reveal=True, prompt="Choose a Supporter card"),
        ),
        Attack(
            title="Dream Dance",
            game_text="Both this Pok\u00e9mon and the Defending Pok\u00e9mon are now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP, self_conditions=(SpecialConditions.ASLEEP,)),
        ),
    ],
)