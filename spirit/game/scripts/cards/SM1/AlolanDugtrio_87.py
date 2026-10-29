from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.attacks_common import snipe_attack


class _TanglingHair(Passive):
    """Your opponent's Active Pokemon's Retreat Cost is [C] more."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        me = carrier_pokemon(carrier)
        if me is not None and pokemon.owning_player_id != me.owning_player_id \
                and is_in_active_spot(pokemon):
            return cost + 1
        return cost


card = PokemonCardDef(
    guid="981f6ddf-f836-5d41-87d6-ae8b6c3f6ec7",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDugtrio.Name",
    display_name="Alolan Dugtrio",
    searchable_by=["Alolan Dugtrio", "Stage 1", "AlolanDugtrio"],
    subtypes=["Stage 1"],
    collector_number=87,
    set_code="SM1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDiglett.Name",
    family_id=50,
    abilities=[
        Ability(
            title="Tangling Hair",
            game_text="Your opponent's Active Pok\u00e9mon's Retreat Cost is Colorless more.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_TanglingHair(),
        ),
        Attack(
            title="Dig Under",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon. This damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=snipe_attack(50, pool='any', apply_modifiers=False),
        ),
    ],
)