from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive
from spirit.game.card_effects.attacks_common import snipe_attack


class MagicRoomPassive(Passive):
    def blocks_trainer_play(self, card, player_id, carrier):
        if player_id == carrier.owning_player_id:
            return False
        if not is_in_active_spot(carrier):
            return False
        return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.ITEM.value


card = PokemonCardDef(
    guid="d03ea72a-df8c-52d1-a1d3-6bf4f2e0099d",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trevenant.Name",
    display_name="Trevenant",
    searchable_by=["Trevenant", "Stage 1", "Trevenant"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name",
    family_id=708,
    abilities=[
        Ability(
            title="Forest's Curse",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent can't play any Item cards from his or her hand.",
            passive=MagicRoomPassive(),
        ),
        Attack(
            title="Tree Slam",
            game_text="This attack does 20 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=snipe_attack(20, count=2, also_base=True),
        ),
    ],
)