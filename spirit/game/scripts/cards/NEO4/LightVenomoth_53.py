from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import mysterious_wing, synchronize


card = PokemonCardDef(
    guid="59f26242-3595-5aed-bb8f-15081d8e5f9d",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightVenomoth.Name",
    display_name="Light Venomoth",
    searchable_by=["Light Venomoth", "Stage 1", "LightVenomoth"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    family_id=48,
    abilities=[
        Attack(
            title="Mysterious Wing",
            game_text="Your opponent may choose a Baby Pok\u00e9mon, Basic Pok\u00e9mon, or Evolution card from his or her discard pile and put it into his or her hand. Either way, you may do the same.",
            cost={PokemonTypes.GRASS: 1},
            effect=mysterious_wing,
        ),
        Attack(
            title="Synchronize",
            game_text="If Light Venomoth and the Defending Pok\u00e9mon have a different number of Energy cards attached to them, this attack does nothing.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=synchronize,
        ),
    ],
)
