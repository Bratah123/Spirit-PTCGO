from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    discard_typed_energy_or_nothing,
    has_typed_basic_energy,
    howl,
)


card = PokemonCardDef(
    guid="64f93940-bfcf-538f-b2f1-17959237c729",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name",
    display_name="Entei",
    searchable_by=["Entei", "Basic", "Entei"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="NEO3",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        Ability(
            title="Howl",
            game_text="When you play Entei from your hand, you may discard the top 5 cards of your deck. (If you have fewer cards in your deck than that, discard all of them.) If any of those are Fire Energy cards, attach them to any of your Fire Pok\u00e9mon of your choice. Using this power ends your turn.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_PLAY,
            ends_turn=True,
            effect=howl,
        ),
        Attack(
            title="Searing Flames",
            game_text="Discard 2 Fire Energy cards attached to Entei or this attack does nothing.",
            cost={PokemonTypes.FIRE: 3},
            damage=60,
            condition=has_typed_basic_energy(PokemonTypes.FIRE, 2),
            effect=discard_typed_energy_or_nothing(PokemonTypes.FIRE, 2),
        ),
    ],
)
