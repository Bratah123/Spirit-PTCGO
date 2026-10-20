from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.content.definitions import def_for
from spirit.game.session.effects import is_pokemon_card


async def _recall(ctx):
    """Choose 1 of this Pokemon's attacks from its previous Evolutions and use it as this attack."""
    seen, candidates = set(), []
    for c in ctx.attacker.children:
        if not is_pokemon_card(c):
            continue
        for a in getattr(def_for(c.archetype_id), "abilities", None) or []:
            if isinstance(a, Attack) and a.title not in seen:
                seen.add(a.title)
                candidates.append((c, a))
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to use")
    if picked is not None:
        await ctx.use_attack(picked[1])


card = PokemonCardDef(
    guid="531bd232-1509-589e-9c78-268e42227539",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=88,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Attack(
            title="Recall",
            game_text="Choose 1 of this Pok\u00e9mon's attacks from its previous Evolutions and use it as this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_recall,
        ),
        Attack(
            title="Combustion Blast",
            game_text="This Pok\u00e9mon can't use Combustion Blast during your next turn.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=None,
            locks_next_turn=True,
        ),
    ],
)