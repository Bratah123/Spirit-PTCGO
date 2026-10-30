from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import leech_seed


card = PokemonCardDef(
    guid="7bec86c7-7561-5d96-813a-302c249278f4",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name",
    display_name="Bulbasaur",
    searchable_by=["Bulbasaur", "Basic", "Bulbasaur"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="BASE4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=1,
    abilities=[
        Attack(
            title="Leech Seed",
            game_text="Unless all damage from this attack is prevented, you may remove 1 damage counter from Bulbasaur.",
            cost={PokemonTypes.GRASS: 2},
            damage=20,
            effect=leech_seed,
        ),
    ],
)
