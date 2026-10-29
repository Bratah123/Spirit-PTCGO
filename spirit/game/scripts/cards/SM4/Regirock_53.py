from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm4 import rock_peak_growl_passive


async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="8b5a84e1-05b4-5a9a-aaa3-5530c38aceee",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regirock.Name",
    display_name="Regirock",
    searchable_by=["Regirock", "Basic", "Regirock"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="SM4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=377,
    abilities=[
        Ability(
            title="Rock Peak Growl",
            game_text="Your Registeel's attacks do 10 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=rock_peak_growl_passive,
        ),
        Attack(
            title="Tough Swing",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            # STUB: attack effect not implemented
            effect=feint,
        ),
    ],
)