from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm12 import blow_away_bomb


card = PokemonCardDef(
    guid="706cdb8b-d2c6-5fc2-968f-4995b19fa838",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    display_name="Koffing",
    searchable_by=["Koffing", "Basic", "Koffing"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=109,
    abilities=[
        Ability(
            title="Blow-Away Bomb",
            game_text="Once during your turn, when you discard this Pok\u00e9mon with the effect of Roxie, you may put 1 damage counter on each of your opponent's Pok\u00e9mon. (Place damage counters after the effect of Roxie.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=blow_away_bomb,
        ),
        Attack(
            title="Poison Gas",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)