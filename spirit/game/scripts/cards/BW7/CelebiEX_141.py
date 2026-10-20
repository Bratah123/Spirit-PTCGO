from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.session.passives import Passive
from spirit.game.content.definitions import def_for, Attack as _AttackDef
from spirit.game.models.board import PokemonEntity


class TimeRecallPassive(Passive):
    """Each of your evolved Pokemon can use any attack from its previous
    Evolutions (Energy costs still apply)."""

    def granted_attacks(self, board, pokemon, carrier):
        if pokemon.owning_player_id != carrier.owning_player_id:
            return []
        attacks, stack = [], [c for c in pokemon.children if isinstance(c, PokemonEntity)]
        while stack:
            prev = stack.pop()
            for ability in getattr(def_for(prev.archetype_id), "abilities", None) or []:
                if isinstance(ability, _AttackDef):
                    attacks.append(ability)
            stack.extend(c for c in prev.children if isinstance(c, PokemonEntity))
        return attacks


card = PokemonCardDef(
    guid="eb92463c-6a29-599f-b19d-069ea2d79b6d",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CelebiEX.Name",
    display_name="Celebi-EX",
    searchable_by=["Celebi-EX", "Basic", "EX", "CelebiEX"],
    subtypes=["Basic", "EX"],
    collector_number=141,
    set_code="BW7",
    rarity=Rarities.RareUltra,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=251,
    abilities=[
        Ability(
            title="Time Recall",
            game_text="Each of your evolved Pok\u00e9mon can use any attack from its previous Evolutions. (You still need the necessary Energy to use each attack.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=TimeRecallPassive(),
        ),
        Attack(
            title="Wind Whisk",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=switch_self_attack(),
        ),
    ],
)