from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import lost_dive, ancient_star

card = PokemonCardDef(
    guid="5cf7a202-67a0-50ac-9616-b354a4f743a7",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AerodactylVSTAR.Name",
    display_name="Aerodactyl VSTAR",
    searchable_by=["Aerodactyl VSTAR", "VSTAR", "AerodactylVSTAR"],
    subtypes=["VSTAR"],
    collector_number=199,
    set_code="SWSH11",
    rarity=Rarities.RareRainbow,
    hp=260,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AerodactylV.Name",
    family_id=142,
    abilities=[
        Attack(
            title="Lost Dive",
            game_text="Put the top 3 cards of your deck in the Lost Zone.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=240,
            effect=lost_dive,
        ),
        Attack(
            title="Ancient Star",
            game_text="Until this Pokémon leaves play, it gains an Ability that has the effect \"Your opponent's Pokémon V in play, except any Aerodactyl VSTAR, have no Abilities.\" (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            vstar=True,
            effect=ancient_star,
        ),
    ],
)
