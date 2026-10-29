from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import damage_all_opponents
from spirit.game.card_effects.sm5 import RotoMotorPassive

card = PokemonCardDef(
    guid="0fad44c1-06e9-52f1-baa3-52393f1103fc",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FanRotom.Name",
    display_name="Fan Rotom",
    searchable_by=["Fan Rotom", "Basic", "FanRotom"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=479,
    abilities=[
        Ability(
            title="Roto Motor",
            game_text="If you have 9 or more Pok\u00e9mon Tool cards in your discard pile, ignore all Energy in the attack cost of each of this Pok\u00e9mon's attacks.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=RotoMotorPassive(),
        ),
        Attack(
            title="Spinning Fan",
            game_text="This attack does 20 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            # STUB: attack effect not implemented
            effect=damage_all_opponents(20),
        ),
    ],
)