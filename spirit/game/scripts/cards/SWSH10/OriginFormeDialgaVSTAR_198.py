from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.pokemon import star_chronos
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy

metal_blast = damage_per(count_energy("self", energy_type=PokemonTypes.METAL), 40, base=40)

card = PokemonCardDef(
    guid="a5fd9650-cdf2-5428-8cae-29858d2ab174",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.OriginFormeDialgaVSTAR.Name",
    display_name="Origin Forme Dialga VSTAR",
    searchable_by=["Origin Forme Dialga VSTAR", "VSTAR", "OriginFormeDialgaVSTAR"],
    subtypes=["VSTAR"],
    collector_number=198,
    set_code="SWSH10",
    rarity=Rarities.RareRainbow,
    hp=280,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.VSTAR,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.OriginFormeDialgaV.Name",
    family_id=483,
    abilities=[
        Attack(
            title="Metal Blast",
            game_text="This attack does 40 more damage for each Metal Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=metal_blast,
        ),
        Attack(
            title="Star Chronos",
            game_text="Take another turn after this one. (Skip Pok\u00e9mon Checkup.) (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.METAL: 4, PokemonTypes.COLORLESS: 1},
            damage=220,
            vstar=True,
            effect=star_chronos,
        ),
    ],
)