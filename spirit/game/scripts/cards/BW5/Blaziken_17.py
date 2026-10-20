from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


card = PokemonCardDef(
    guid="848868c4-a390-5470-bf4d-5cda25bd02f4",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blaziken.Name",
    display_name="Blaziken",
    searchable_by=["Blaziken", "Stage 2", "Blaziken"],
    subtypes=["Stage 2"],
    collector_number=17,
    set_code="BW5",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    family_id=255,
    abilities=[
        Attack(
            title="Blaze Kick",
            game_text="Flip a coin. If heads, this attack does 30 more damage. If tails, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)