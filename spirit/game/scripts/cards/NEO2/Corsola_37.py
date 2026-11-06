from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import (
    has_typed_basic_energy, recover_discarding_energy,
)


card = PokemonCardDef(
    guid="1ebd7c91-648b-5a16-97ce-2ce92d90eddb",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corsola.Name",
    display_name="Corsola",
    searchable_by=["Corsola", "Basic", "Corsola"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=222,
    abilities=[
        Attack(
            title="Recover",
            game_text="Discard 1 Water Energy card attached to Corsola or this attack does nothing. Remove all damage counters from Corsola.",
            cost={PokemonTypes.WATER: 1},
            condition=has_typed_basic_energy(PokemonTypes.WATER),
            effect=recover_discarding_energy(PokemonTypes.WATER),
        ),
        Attack(
            title="Spike Cannon",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=30),
        ),
    ],
)
