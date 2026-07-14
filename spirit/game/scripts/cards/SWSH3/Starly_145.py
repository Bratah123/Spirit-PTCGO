from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive
from spirit.game.card_effects.support_common import search_to_hand


class _SkyCircusPassive(Passive):
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        state = getattr(board, "turn_state", None)
        if state and any(name == "Bird Keeper" for _, name, _ in state.trainers_played):
            return {}
        return cost


card = PokemonCardDef(
    guid="0be748d9-42d7-51c6-81aa-9daefb441bc2",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starly.Name",
    display_name="Starly",
    searchable_by=["Starly", "Basic", "Starly"],
    subtypes=["Basic"],
    collector_number=145,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=396,
    abilities=[
        Ability(
            title="Sky Circus",
            game_text="If you played Bird Keeper from your hand during this turn, ignore all Energy in this Pok\u00e9mon's attack costs.",
            passive=_SkyCircusPassive(),
        ),
        Attack(
            title="Keen Eye",
            game_text="Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=search_to_hand(count=2),
        ),
    ],
)