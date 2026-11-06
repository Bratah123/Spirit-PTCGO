from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn, is_in_active_spot
from spirit.game.session.passives import Passive, carrier_pokemon


class _MetalFortress(Passive):
    """Prevent all effects of the opponent's attacks, including damage, done to your Benched Pokemon."""
    def _covers(self, target, carrier):
        me = carrier_pokemon(carrier)
        return me is not None and target.owning_player_id == me.owning_player_id and not is_in_active_spot(target)

    def prevents_damage(self, calc, carrier):
        return calc.is_attack and calc.is_opposing and self._covers(calc.target, carrier)

    def blocks_attack_effects(self, target, carrier):
        return self._covers(target, carrier)


card = PokemonCardDef(
    guid="f18b1888-af01-5cbf-9b06-4a25c48b6329",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1", "Bronzong"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=436,
    abilities=[
        Ability(
            title="Metal Fortress",
            game_text="Prevent all effects of your opponent's attacks, including damage, done to your Benched Pok\u00e9mon.",
            passive=_MetalFortress(),
        ),
        Attack(
            title="Guard Press",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=protect_next_turn(reduce=20),
        ),
    ],
)