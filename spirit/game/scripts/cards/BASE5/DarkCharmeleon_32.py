from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import fireball, has_fire_energy_attached


card = PokemonCardDef(
    guid="bb99756f-bc23-5bf6-a16b-bfb9333fcf47",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkCharmeleon.Name",
    display_name="Dark Charmeleon",
    searchable_by=["Dark Charmeleon", "Stage 1", "DarkCharmeleon"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Tail Slap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Fireball",
            game_text="Use this attack only if there are any Fire Energy cards attached to Dark Charmeleon. Flip a coin. If heads, discard 1 of those Energy cards. If tails, this attack does nothing (not even damage).",
            cost={PokemonTypes.FIRE: 3},
            damage=70,
            condition=has_fire_energy_attached,
            effect=fireball,
        ),
    ],
)
