from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm6 import diamond_rain, princess_cheers_passive

card = PokemonCardDef(
    guid="6eb6ea32-5340-53d6-b32a-53a8ce66fd29",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DianciePrismStar.Name",
    display_name="Diancie {*}",
    searchable_by=["Diancie {*}", "Basic", "Prism Star", "DianciePrismStar"],
    subtypes=["Basic", "Prism Star"],
    collector_number=74,
    set_code="SM6",
    rarity=Rarities.Prism,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=719,
    abilities=[
        Ability(
            title="Princess's Cheers",
            game_text="As long as this Pok\u00e9mon is on your Bench, your Fighting Pok\u00e9mon's attacks do 20 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=princess_cheers_passive,
        ),
        Attack(
            title="Diamond Rain",
            game_text="Heal 30 damage from each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=90,
            effect=diamond_rain,
        ),
    ],
)
