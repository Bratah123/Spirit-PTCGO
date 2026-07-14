from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive
from spirit.game.card_effects.attacks_common import snipe_attack


class _SkyCircusPassive(Passive):
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        state = getattr(board, "turn_state", None)
        if state and any(name == "Bird Keeper" for _, name, _ in state.trainers_played):
            return {}
        return cost


card = PokemonCardDef(
    guid="e35c2272-428c-5c09-a29e-f112deb739f9",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rowlet.Name",
    display_name="Rowlet",
    searchable_by=["Rowlet", "Basic", "Rowlet"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="SWSH3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=722,
    abilities=[
        Ability(
            title="Sky Circus",
            game_text="If you played Bird Keeper from your hand during this turn, ignore all Energy in this Pok\u00e9mon's attack costs.",
            passive=_SkyCircusPassive(),
        ),
        Attack(
            title="Wind Shard",
            game_text="This attack does 60 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=snipe_attack(60, pool="bench"),
        ),
    ],
)