"""STUB: effect not implemented — do not guess mechanics.
Luvdisc (EX5 #40): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.ex import loving_draw, poke_power_condition, sweet_temptation

card = PokemonCardDef(
    guid="34a95748-c3d1-5693-bf3b-44cd706b684c",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luvdisc.Name",
    display_name="Luvdisc",
    searchable_by=["Luvdisc", "Basic", "Luvdisc"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=370,
    abilities=[
        Ability(
            title="Loving Draw",
            game_text="Draw cards until you have the same number of cards in your hand as your opponent has in his or her hand.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=loving_draw(),
        ),
        Attack(
            title="Sweet Temptation",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with 1 of the Defending Pok\u00e9mon. Your opponent chooses the Defending Pok\u00e9mon to switch. This attack does 10 damage to the new Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=sweet_temptation(),
        ),
    ],
)