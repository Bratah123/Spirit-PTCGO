from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import smokescreen_attack
from spirit.game.card_effects.ecard import SuctionCupsPassive


card = PokemonCardDef(
    guid="702e9606-27c0-5c9c-844b-90f954b36b86",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Octillery.Name",
    display_name="Octillery",
    searchable_by=["Octillery", "Stage 1", "Octillery"],
    subtypes=["Stage 1"],
    collector_number=170,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    family_id=223,
    abilities=[
        Ability(
            title="Suction Cups",
            game_text="As long as Octillery is your Active Pok\u00e9mon, whenever the Defending Pok\u00e9mon retreats, discard all Energy cards attached to the Defending Pok\u00e9mon when it goes to the Bench.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=SuctionCupsPassive(),
        ),
        Attack(
            title="Smokescreen",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=smokescreen_attack(),
        ),
    ],
)
