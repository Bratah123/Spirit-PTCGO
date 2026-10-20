"""STUB: effect not implemented — do not guess mechanics.
Vileplume (XY7 #3): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive
from spirit.game.session.effects import is_item_card


class _IrritatingPollen(Passive):
    """Each player can't play any Item cards from his or her hand."""
    def blocks_trainer_play(self, card, player_id, carrier):
        return is_item_card(card)


card = PokemonCardDef(
    guid="799bb55d-d79b-5cd6-91d1-f25af840b56b",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name",
    display_name="Vileplume",
    searchable_by=["Vileplume", "Stage 2", "Vileplume"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="XY7",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Irritating Pollen",
            game_text="Each player can't play any Item cards from his or her hand.",
            # STUB: ability effect not implemented
            passive=_IrritatingPollen(),
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)