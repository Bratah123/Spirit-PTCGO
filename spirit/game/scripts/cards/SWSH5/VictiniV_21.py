from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import (
    bonus_if, defender_is_v, self_energy_discard_attack,
)

card = PokemonCardDef(
    guid="e368e757-543c-5505-bffe-d017bd259890",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VictiniV.Name",
    display_name="Victini V",
    searchable_by=["Victini V", "Basic", "V", "VictiniV"],
    subtypes=["Basic", "V"],
    collector_number=21,
    set_code="SWSH5",
    rarity=Rarities.RareHoloV,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=494,
    abilities=[
        Attack(
            title="V Bullet",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon V, this attack does 50 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator="+",
            effect=bonus_if(defender_is_v, 50),
        ),
        Attack(
            title="Flare Shot",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)