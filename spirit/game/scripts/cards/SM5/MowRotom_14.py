from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
from spirit.game.card_effects.sm5 import RotoMotorPassive

card = PokemonCardDef(
    guid="bed91645-0fba-5e32-a887-8f2faff9ef05",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MowRotom.Name",
    display_name="Mow Rotom",
    searchable_by=["Mow Rotom", "Basic", "MowRotom"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="SM5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=479,
    abilities=[
        Ability(
            title="Roto Motor",
            game_text="If you have 9 or more Pok\u00e9mon Tool cards in your discard pile, ignore all Energy in the attack cost of each of this Pok\u00e9mon's attacks.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=RotoMotorPassive(),
        ),
        Attack(
            title="Special Mow",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=discard_opponent_energy_attack(special_only=True),
        ),
    ],
)