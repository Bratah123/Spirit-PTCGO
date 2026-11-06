from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import strange_tentacles, strange_tentacles_condition


card = PokemonCardDef(
    guid="faf1f5c8-52fd-51f7-8bc9-408976dc0a67",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacruel.Name",
    display_name="Tentacruel",
    searchable_by=["Tentacruel", "Stage 1", "Tentacruel"],
    subtypes=["Stage 1"],
    collector_number=176,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name",
    family_id=72,
    abilities=[
        Ability(
            title="Strange Tentacles",
            game_text="Once during your turn (before your attack), as long as the number of Energy cards attached to the Defending Pok\u00e9mon is less than the number of Energy cards attached to your Active Pok\u00e9mon, you may choose an Energy card, if any, in your opponent's discard pile and attach it to the Defending Pok\u00e9mon. This power can't be used if Tentacruel is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=strange_tentacles_condition,
            effect=strange_tentacles,
        ),
        Attack(
            title="Poison Sting",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
    ],
)
