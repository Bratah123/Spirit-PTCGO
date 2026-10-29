from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import rock_crush
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


card = PokemonCardDef(
    guid="452e6fb9-9f5f-5d97-9776-b590a05cea24",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LycanrocGX.Name",
    display_name="Lycanroc-GX",
    searchable_by=["Lycanroc-GX", "Stage 1", "GX", "LycanrocGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=136,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name",
    family_id=745,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=rock_crush,
        ),
        Attack(
            title="Accelerock",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
        Attack(
            title="Lycanfang-GX",
            game_text="Discard 2 Energy from this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)
