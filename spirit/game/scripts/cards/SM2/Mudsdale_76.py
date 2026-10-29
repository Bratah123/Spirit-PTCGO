from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_tool, recoil_attack

card = PokemonCardDef(
    guid="12595a18-c8e6-56a7-9705-1882f175a9a9",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mudsdale.Name",
    display_name="Mudsdale",
    searchable_by=["Mudsdale", "Stage 1", "Mudsdale"],
    subtypes=["Stage 1"],
    collector_number=76,
    set_code="SM2",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mudbray.Name",
    family_id=749,
    abilities=[
        Attack(
            title="Enhanced Stomp",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool card attached to it, this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.attacker is not None and has_tool(ctx.attacker), 60),
        ),
        Attack(
            title="High Horsepower",
            game_text="This Pok\u00e9mon does 40 damage to itself.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=recoil_attack(40),
        ),
    ],
)