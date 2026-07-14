from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.pokemon import is_energy_card
from spirit.game.card_effects.support_common import attach_from_discard, requires_discard


def is_darkness_energy_card(card):
    return is_energy_card(card) and PokemonTypes.DARKNESS.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="cdac4f88-0afe-5c44-b0a4-997224129fab",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMoltresV.Name",
    display_name="Galarian Moltres V",
    searchable_by=["Galarian Moltres V", "Basic", "V", "GalarianMoltresV"],
    subtypes=["Basic", "V"],
    collector_number=97,
    set_code="SWSH6",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=146,
    abilities=[
        Ability(
            title="Direflame Wings",
            game_text="Once during your turn, you may attach a Darkness Energy card from your discard pile to this Pok\u00e9mon. You can't use more than 1 Direflame Wings Ability each turn.",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Direflame Wings",
            condition=requires_discard(is_darkness_energy_card),
            effect=attach_from_discard(predicate=is_darkness_energy_card, count=1, target="self"),
        ),
        Attack(
            title="Aura Burn",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=recoil_attack(30),
        ),
    ],
)