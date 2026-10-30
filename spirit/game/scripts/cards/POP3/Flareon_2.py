from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ex import (
    attached_basic_energy_at_least, discard_basic_energy_attack,
)


card = PokemonCardDef(
    guid="1a1b8b01-7606-5ca3-86cb-a691d85ca768",
    key="POP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon",
    searchable_by=["Flareon", "Stage 1", "Flareon"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="POP3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 2 basic Energy cards attached to Flareon or this attack does nothing.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            condition=attached_basic_energy_at_least(2),
            effect=discard_basic_energy_attack(2),
        ),
    ],
)
