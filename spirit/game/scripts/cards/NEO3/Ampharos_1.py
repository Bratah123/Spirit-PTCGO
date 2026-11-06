from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import attract_current


card = PokemonCardDef(
    guid="635602fb-00ef-5970-8590-85655bb373ee",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharos.Name",
    display_name="Ampharos",
    searchable_by=["Ampharos", "Stage 2", "Ampharos"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="NEO3",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=180,
    abilities=[
        Attack(
            title="Attract Current",
            game_text="Flip 3 coins. For each heads, you may search your deck for a Lightning Energy card and attach it to 1 of your Lightning Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=attract_current,
        ),
        Attack(
            title="Gigavolt",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 20 more damage. If tails, this attack does 40 damage and the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=condition_attack(
                flip=True,
                tails_conditions=(SpecialConditions.PARALYZED,),
                heads_bonus_damage=20,
            ),
        ),
    ],
)
