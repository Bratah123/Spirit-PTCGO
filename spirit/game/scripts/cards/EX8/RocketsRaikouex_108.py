"""STUB: effect not implemented — do not guess mechanics.
Rocket's Raikou ex (EX8 #108): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import lightning_burst_on_dark_attach, thunderous_blow


card = PokemonCardDef(
    guid="c84144a7-d1c4-551a-b792-fca59c4bb542",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsRaikouex.Name",
    display_name="Rocket's Raikou ex",
    searchable_by=["Rocket's Raikou ex", "Basic", "ex", "RocketsRaikouex"],
    subtypes=["Basic", "ex"],
    collector_number=108,
    set_code="EX8",
    rarity=Rarities.RareSecret,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=243,
    abilities=[
        Ability(
            title="Lightning Burst",
            game_text="Whenever you attach a Darkness Energy card from your hand to Rocket's Raikou ex, you may choose 1 of the Defending Pok\u00e9mon and switch it with 1 of your opponent's Benched Pok\u00e9mon. Your opponent chooses the Benched Pok\u00e9mon to switch. This power can't be used if Rocket's Raikou ex is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            passive=lightning_burst_on_dark_attach(),
        ),
        Attack(
            title="Thunderous Blow",
            game_text="Does 40 damage plus 10 more damage for each Lightning Energy attached to Rocket's Raikou ex.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=thunderous_blow(),
        ),
    ],
)